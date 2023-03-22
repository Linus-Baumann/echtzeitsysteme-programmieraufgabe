import { Component } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import {range} from "rxjs";

@Component({
  selector: 'app-diagram-display',
  templateUrl: './diagram-display.component.html',
  styleUrls: ['./diagram-display.component.scss']
})
export class DiagramDisplayComponent {
  currentGraph = 0
  graph_buffer: any[] = [];
  private isImageLoading = false;
  public firstGraphIsShown = true;

  constructor(private httpClient: HttpClient) {
  }
  ngOnInit(): void {
    this.extendGraphBuffer(5)
  }

  createImageFromBlob(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
      this.graph_buffer.push(reader.result);
      console.log("New bufferlength: " + this.graph_buffer.length)
    }, false);

    if (image) {
      reader.readAsDataURL(image);
    }
  }

  private extendGraphBuffer(bufferSize=1): void {
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
    if ((this.graph_buffer.length - this.currentGraph) < 5) {
      this.extendGraphBuffer()
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
}
