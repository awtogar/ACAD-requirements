function myFunction() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();
  var lastColumn = sheet.getLastColumn();
  var lastRow = sheet.getLastRow();
  var emptyColumn = -1;

  for (var col = 1; col <= lastColumn; col++) {
    var isEmpty = true;
    for (var row = 1; row <= lastRow; row++) {
      var cellValue = sheet.getRange(row, col).getValue();
      if (cellValue !== "") {
        isEmpty = false;
        break;
      }
    }
    if (isEmpty) {
      emptyColumn = col;
      break;
    }
  }

  if (emptyColumn == -1) {
    emptyColumn = lastColumn + 1;
  }

  sheet.getRange(1, emptyColumn).setValue("FileName");
  sheet.getRange(1, emptyColumn + 1).setValue("FileLink");

  var folder = DriveApp.getFolderById("id drive disini");
  var files = folder.getFiles();
  var data = [];

  while (files.hasNext()) {
    var file = files.next();
    var name = file.getName();
    var url = file.getUrl();
    data.push([name, url]);
  }
  if (data.length > 0) {
    sheet.getRange(2, emptyColumn, data.length, 2).setValues(data);
  }
}
