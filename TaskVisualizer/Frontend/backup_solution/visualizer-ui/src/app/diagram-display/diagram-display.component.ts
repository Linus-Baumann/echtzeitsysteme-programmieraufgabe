import {Component, OnInit} from '@angular/core';
import { HttpClient } from "@angular/common/http";
import {MatDialog} from "@angular/material/dialog";
import {ErrorDialogComponent} from "./error-dialog/error-dialog.component";

@Component({
  selector: 'app-diagram-display',
  templateUrl: './diagram-display.component.html',
  styleUrls: ['./diagram-display.component.scss']
})
export class DiagramDisplayComponent implements OnInit{
  currentGraph = 0;
  graphBuffer: any[] = [];
  configList: string[] = [];
  private isImageLoading = false;
  public firstGraphIsShown = true;
  private bufferIsUpdating = false;

  constructor(
    private httpClient: HttpClient,
    public dialog: MatDialog) {
  }
  ngOnInit(): void {
    this.resetDiagram()
    this.updateConfigList()
  }

  private openDialog(enterAnimationDuration: string, exitAnimationDuration: string): void {
    this.dialog.open(ErrorDialogComponent, {
      width: '250px',
      enterAnimationDuration,
      exitAnimationDuration,
    });
  }

  private createImageFromBlob(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
      this.graphBuffer.push(reader.result);
      console.log("New bufferlength: " + this.graphBuffer.length)
    }, false);

    if (image) {
      reader.readAsDataURL(image);
    }
  }

  private updateGraphBuffer(bufferSize=1, fromUpdateProcess=false): void {
    if (!this.bufferIsUpdating || fromUpdateProcess) {
      this.bufferIsUpdating = true;
      this.httpClient.get('/visualizer-api/diagram', { responseType: 'blob' }).subscribe(data => {
        this.createImageFromBlob(data);
        this.isImageLoading = false;
        if (bufferSize > 1) {
          this.updateGraphBuffer(bufferSize-1, true);
        }
        else {
          this.bufferIsUpdating = false
        }
      });
    }
  }

  public nextGraph(): void {
    this.currentGraph += 1
    if (this.currentGraph == 1) {
      this.firstGraphIsShown = false
    }
    if ((this.graphBuffer.length - this.currentGraph) < 10) {
      this.updateGraphBuffer(5)
    }
  }

  public previousGraph(): void {
    if (this.currentGraph == 0) {
      return
    } else {
      this.currentGraph -= 1
    }
    if (this.currentGraph == 0) {
      this.firstGraphIsShown = true
    }
  }

  public resetDiagram(): void {
    this.graphBuffer = []
    this.httpClient.get("/visualizer-api/reset-diagram").subscribe( data => {
      console.log("Diagram was reset (" + data + ")")
      if (data.toString() == "Error") {
        console.log("Ddddddddddddd")
        this.openDialog('500', '1000')
      }
      this.currentGraph = 0
      this.updateGraphBuffer(5)
    })
  }

  public updateConfiguration(config: string): void {
    this.graphBuffer = []
    this.httpClient.get("/visualizer-api/update-config?config-name=" + config).subscribe( data => {
      console.log("New Configuration (" + data + ")")
      if (data.toString() == "Error") {
        console.log("Ddddddddddddd")
        this.openDialog('500', '1000')
      }
      this.currentGraph = 0
      this.updateGraphBuffer(5)
    })
  }

  public updateConfigList(): void {
    this.httpClient.get("/visualizer-api/config-list").subscribe( data => {
      let buffer: string[] = []
      if (Array.isArray(data)) {
        data.forEach( function (file) {
          if (typeof file === 'string' && file.endsWith('.csv')) {
            buffer.push(file)
          }
        })
      }
      this.configList = buffer
      console.log("Updated configuration list: " + this.configList)
    })
  }
}
