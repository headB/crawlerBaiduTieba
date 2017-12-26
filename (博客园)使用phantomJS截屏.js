// a phantomjs example
var page = require('webpage').create();
phantom.outputEncoding="gbk";
page.viewportSize = { width: 1920, height: 1080 };
page.open("http://www.cnblogs.com/front-Thinking", function(status) {
if ( status === "success" ) {
        console.log(page.title); 
        page.render("front-Thinking.png");
     } else {
        console.log("Page failed to load."); 
     }
    phantom.exit(0);
 });
