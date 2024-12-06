<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BuyRight AI</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <div id="chatai" class="contact-section">
        <div id="assistance" class="chat-container">
            <div class="chat-box" id="chat-box"></div>
            <input type="text" id="userInput" placeholder="Type your message...">
            <button onclick="sendMessage()" class="btn11">Send</button>
        </div>
    
        <div class="info-container">
            <h3><b>Try Our <span style="background-color:#15F5BA ; color:white;">Shoppingsmart bot </span> Assistance for Free</b></h3>
            <p>Engage in a conversation with ShopSaz powered by NVIDIA Riva, and explore its capabilities firsthand. Experience personalized shopping assistance and see how Buyright AI, can enhance your shopping experience and support your needs.</p>
            <div class="ctbtn">
            <a href="https://www.shoppingsmartinfo.com/contact/" class="btn11">Get Full Access</a>
          </div>
        </div>
    </div>
    <div id="chatai" class="contact-section">
       
        <div id="visual" class="info-container">
            <h3><b>Feed an image to<span style="background-color: #15F5BA; color:white;"> BuyRight AI </span> </b></h3>
            <p>Engage in a Visual Search of a product with BuyRight AI powered by NVIDIA Deepstream, and explore its capabilities firsthand. Experience personalized shopping assistance and see how BuyRight AI, can enhance your shopping experience and support your needs.</p>
            <div class="ctbtn">
            <a href="https://www.shoppingsmartinfo.com/contact/" class="btn11">Get Full Access</a>
       </div>
        </div>
        <div class="chat-container">
            <div class="upimg" id="upimg"></div>
            <p>Upload an image to see visual search in action</p>
            <form id="imageUploadForm" action="/upload" method="post" enctype="multipart/form-data" class="">
               
                <input class="" type="file" name="image" accept="image/*">
                <button class="btn11" type="submit" class="btn">Upload Image</button>
            </form> </div>
       
    
        
    </div>
    <script src="script.js"></script>
</body>
</html>
