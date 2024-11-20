(function() {
    // Ambil dokumen yang aktif
        var doc = app.activeDocument;
    
    // Atur preset pdf yang bakalan diexport
        var pdfExportPreset = app.pdfExportPresets.item("[High Quality Print]");
    
    // Pilih CSV yg mau diload
        var csvFile = File.openDialog("Pilih CSV File");
        if (csvFile == null) {
            alert("Gak ada CSV yang dipilih. Script Batal");
            return;
        }
    
    // Baca File CSV dan exract kode column
        var csvData = readCSV(csvFile);
        if (csvData == null || csvData.length == 0) {
            alert("CSV file kosong atau ada kesalahan.");
            return;
        }
    
    // Pop up buat milih dimana ouput bakal disimpan
        var outputFolder = Folder.selectDialog("Select folder to save PDFs");
    
        if (outputFolder == null) {
            alert("No folder selected. Script canceled.");
            return;
        }
    
    // Ngemastiin jumlah pages sama dengan jumlah data column kode di csv
        if (csvData.length < doc.pages.length) {
            alert("CSV data contains fewer entries than document pages.");
            return;
        }
    
        // Lakuin perulangan buat setiap pages dan export sebagai pdf terpisah dengan values kode
        // TODO:
        for (var i = 0; i < doc.pages.length; i++) {
            var page = doc.pages[i];
    
            // Get the kode for this page from the CSV
            var rawFileName = csvData[i].kode;
            var cleanFileName = sanitizeFileName(rawFileName) + ".pdf"; // Sanitize the file name
            var pdfFile = new File(outputFolder + "/" + cleanFileName);
    
            // Set the page range (only current page)
            app.pdfExportPreferences.pageRange = page.name;
    
            // Export the page as a PDF with the sanitized kode name
            doc.exportFile(ExportFormat.pdfType, pdfFile, false, pdfExportPreset);
        }
    
        // Reset the page range to all pages after export is done
        app.pdfExportPreferences.pageRange = "[All]";
    
        alert("Export complete! PDFs have been named using the kode from the CSV.");
    
        // Function to read CSV file and return an array of objects
        function readCSV(file) {
            file.open('r');
            var data = [];
            var headers = [];
    
            // Read headers
            if (!file.eof) {
                headers = file.readln().split(",");
            }
    
            // Read each line of the CSV
            while (!file.eof) {
                var line = file.readln().split(",");
                var rowData = {};
                for (var j = 0; j < headers.length; j++) {
                    rowData[headers[j]] = line[j];
                }
                data.push(rowData);
            }
    
            file.close();
            return data;
        }
    
        // Function to sanitize file names (replace invalid characters)
        function sanitizeFileName(fileName) {
            return fileName.replace(/[\/\\:?\*"<>\|]/g, "_"); // Replace invalid characters with "_"
        }
    
    })();
    