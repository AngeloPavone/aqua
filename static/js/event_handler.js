var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function(){
    socket.emit('message_event',{
        network_log: 'User Connected'
    })
        var form = $('form.chatbox').on('submit', function(e){
            e.preventDefault()
            let user_input = $('#message').val()
            socket.emit('message_event',{
                chat_log: user_input
            })
            $('#message').val("").focus()
        })
    })
    socket.on('my response', function(msg) {
        console.log(msg)
        $('.chat_history').text(msg)
})
