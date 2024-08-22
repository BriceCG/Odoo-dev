odoo.define('product_file_preview', function(require){
    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');
    publicWidget.registry.ProductFilePreview = publicWidget.Widget.extend({
        selector: '.oe_website_sale',
        events: {
            'click .btn.website_preview_pdf': '_previewPdf'
        },
        start: function(){
            var self = this;
            var product_id = self.$el.find('.website_preview_pdf').attr('product-id');
            console.log(product_id)
            product_id = parseInt(product_id);
            var def =  ajax.rpc('/get-product-attachment',{"product_id": product_id}).then(function(data){
                self.attachment = data.attachment
            })
            return Promise.all([def, this._super.apply(this, arguments)]);
        },
        _previewPdf: function(ev){
            ev.preventDefault();
            var product_id = $(ev.currentTarget).attr('product-id');
            product_id = parseInt(product_id);
            var self = this;
            this.openCanvasPdf()
        },
        openCanvasPdf: function(){
            var self = this;
            var pdfData = atob(self.attachment);
            // The workerSrc property shall be specified.
            pdfjsLib.GlobalWorkerOptions.workerSrc = '//mozilla.github.io/pdf.js/build/pdf.worker.mjs';
            // Using DocumentInitParameters object to load binary data.
            var loadingTask = pdfjsLib.getDocument({data: pdfData});
            loadingTask.promise.then(function(pdf) {
                console.log('PDF loaded');

                // Fetch the first page
                var pageNumber = 1;
                pdf.getPage(pageNumber).then(function(page) {
                console.log('Page loaded');
                var scale = 1.5;
                var viewport = page.getViewport({scale: scale});

                  // Prepare canvas using PDF page dimensions
                  var canvas = document.getElementById('canvas_pdf');
                  var context = canvas.getContext('2d');
                  canvas.height = viewport.height;
                  canvas.width = viewport.width;

                  // Render PDF page into canvas context
                  var renderContext = {
                    canvasContext: context,
                    viewport: viewport
                  };
                  var renderTask = page.render(renderContext);
                  renderTask.promise.then(function () {
                    console.log('Page rendered');
                  });
                });
              }, function (reason) {
                // PDF loading error
                console.error(reason);
              });
        }
    });
    return publicWidget.registry.ProductFilePreview;
});