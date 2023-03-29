import { Component } from '@angular/core';
import {MatDialogRef} from "@angular/material/dialog";

class DialogAnimationsExampleDialog {
}

@Component({
  selector: 'app-error-dialog',
  templateUrl: './error-dialog.component.html',
  styleUrls: ['./error-dialog.component.scss']
})
export class ErrorDialogComponent {
  constructor(public dialogRef: MatDialogRef<DialogAnimationsExampleDialog>) {}
}
