var minus = document.querySelector('#minus'),
    plus = document.querySelector('#plus'),
    value = document.querySelector('#value'),
    users = document.querySelector('#users'),
    connect = document.querySelector('#connect'),
    disconnect = document.querySelector('#disconnect'),
    ws_Server = document.querySelector('#wsServer'),
    log = document.querySelector('#log').innerHTML,
    rangePercent = $('#slider').val(),
    websocket;

var update_color_fcn = function(){
    rangePercent = $('[type="range"]').val();
    $('[class="slider_value"]').text(rangePercent);
    $('#slider').css('filter', 'hue-rotate(-' + rangePercent + 'deg)');
}

$('#slider').on('change input', function() {
    update_color_fcn()
    if (websocket!=null){
        websocket.send(JSON.stringify({slider: rangePercent}));
    }
});

connect.onclick = function() {
        websocket = new WebSocket(ws_Server.value);

        websocket.onopen = function() {
            log = ''
            log = ('<li><span class="badge badge-success">websocket opened</span></li>');
            ws_Server.disabled = true;
            connect.disabled = true;
            disconnect.disabled = false;
        };

        websocket.onerror = function() {
            log =''
            log =('<li><span class="badge badge-important">websocket error</span></li>');
        };

        websocket.onmessage = function (event) {
            data = JSON.parse(event.data);
            switch (data.type) {
                case 'state':
                    value.textContent = data.counter;
                    $('#slider').val(data.slider)
                    update_color_fcn()
                    break;

                case 'users':
                    users.textContent = (
                        data.count.toString() + " user" +
                        (data.count == 1 ? "" : "s"));
                    break;
                default:
                    console.error(
                        "unsupported event", data);
            }
            log =''
            log =('<li>Received new '+data.type+' event</li>');
        };

        //websocket = new WebSocket("ws://192.168.1.12:80/")
        minus.onclick = function (event) {
            if (websocket!=null){
              websocket.send(JSON.stringify({action: 'minus'}));
            }
        }
        
        plus.onclick = function (event) {
            if (websocket!=null){
                websocket.send(JSON.stringify({action: 'plus'}));
            }
        }
        
        websocket.onclose = function() {
            log =''
            log =('<li><span class="badge badge-important">websocket closed</span></li>');
            ws_Server.disabled = false;
            connect.disabled = false;
            disconnect.disabled = true;
            
            users.textContent = ("? user");
            value.textContent = ("?")
        };
    return false;
};

disconnect.onclick = function() {
    websocket.close();
    websocket = null
    return false;
};
