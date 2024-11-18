function myFunction() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();
  // Mulai dari baris aktif
  var startRow = sheet.getActiveCell().getRow();
  // Masukin id lokasi drive
  var folder = DriveApp.getFolderById("1YhtlWa29jL4b2QJXfy8n36qgTSjmWO4K");
  var files = folder.getFiles();
  
  // set jadi data array
  var data = [];
  var row = startRow; // Mulai dari baris yang aktif di spreadsheet
  while (files.hasNext()) {

    var file = files.next();
    // Dapetin nama file
    var name = file.getName();
     // Dapetin URL file
    var url = file.getUrl();     
    
    data.push([name, url]); 
  }

  // Set header
  /// Masukin nama file dari google drive ke Column J dan kasih nama header _PDF lalu dengan row isi nama gdrive file nya
  /// Masukin url file dari google drive ke Column J dan kasih nama header _Link lalu dengan row isi link gdrive file nya

  sheet.getRange(startRow, 10).setValue("_PDF");
  sheet.getRange(startRow, 11).setValue("_Link");

  // Masukin data ke baris pertama setelah header
  if (data.length > 0) {
    sheet.getRange(startRow + 1, 10, data.length, 2).setValues(data);  
  }
}
