import { Component } from '@angular/core';
import { HttpClient } from "@angular/common/http";

@Component({
  selector: 'app-diagram-display',
  templateUrl: './diagram-display.component.html',
  styleUrls: ['./diagram-display.component.scss']
})
export class DiagramDisplayComponent {
  currentGraph = 0
  graphBuffer: any[] = [];
  private isImageLoading = false;
  public firstGraphIsShown = true;

  constructor(private httpClient: HttpClient) {
  }
  ngOnInit(): void {
    this.resetDiagram()
  }

  createImageFromBlob(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
      this.graphBuffer.push(reader.result);
      console.log("New bufferlength: " + this.graphBuffer.length)
    }, false);

    if (image) {
      reader.readAsDataURL(image);
    }
  }

  private updateGraphBuffer(bufferSize=1): void {
    for (let round = 0; round < bufferSize; round++) {
      this.httpClient.get('/visualizer-api/diagram', { responseType: 'blob' }).subscribe(data => {
        this.createImageFromBlob(data);
        this.isImageLoading = false;
      });
    }
  }

  public nextGraph(): void {
    this.currentGraph += 1
    if (this.currentGraph == 1) {
      this.firstGraphIsShown = false
    }
    if ((this.graphBuffer.length - this.currentGraph) < 5) {
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
    this.httpClient.get("/visualizer-api/reset-diagram").subscribe( data => {
      console.log("Diagram was reset (" + data + ")")
      this.currentGraph = 0
      this.graphBuffer = []
      this.updateGraphBuffer()
    })

  }

  public readNewFile(): void {
    this.graphBuffer = []
    this.httpClient.get("/visualizer-api/read-file").subscribe( data => {
      console.log("New File Input (" + data + ")")
      this.currentGraph = 0
      this.updateGraphBuffer()
    })

  }
}
