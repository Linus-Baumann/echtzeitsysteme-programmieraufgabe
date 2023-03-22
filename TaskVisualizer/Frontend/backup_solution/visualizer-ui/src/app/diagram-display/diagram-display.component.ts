import { Component } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import {range} from "rxjs";

@Component({
  selector: 'app-diagram-display',
  templateUrl: './diagram-display.component.html',
  styleUrls: ['./diagram-display.component.scss']
})
export class DiagramDisplayComponent {
  current_graph = "assets/data/graph_buffer/test.png"
  graph_buffer: any[] = [];
  private isImageLoading = false;

  constructor(private httpClient: HttpClient) {
  }
  ngOnInit(): void {
    this.extendGraphBuffer(5)
  }

  createImageFromBlob(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
      this.graph_buffer.push(reader.result);
    }, false);

    if (image) {
      reader.readAsDataURL(image);
    }
  }

  public extendGraphBuffer(buffer_size=1): void {
    for (let index in range(buffer_size)) {
      this.httpClient.get('/visualizer-api/diagram', { responseType: 'blob' }).subscribe(data => {
        this.createImageFromBlob(data);
        this.isImageLoading = false;
      });
    }
    console.log("New buffer: " + this.graph_buffer)
  }
}
