    var questions;
    var atual;
    var totalAtual;
    var validas;
    var questionAtual;
    var total;
$(function() {
    $('#start').click(function(){
        $.ajax({
            url: '/questions/',
            success: function(data) {
                atual = 0;
                totalAtual = 0;
                validas = 0;
                $('body').removeClass('home')
                $('.opinar, #header').show()
                $('#texto p').html('')
                $('#start').hide()
                questions = data;
                total = questions.length;
                question();
                atualizarContador()
            }
        });
    });

    $('.opinar').click(function(){
        totalAtual++;
        certa = (questionAtual.fields.lugar)?'ufpel':questionAtual.fields.outro;
        if($(this).attr('data-opina') == certa){
            validas++;
        }
        validar();
    });

    $('#restart').click(function(){
        $(this).hide();
        $('#start').show().trigger('click')
    })

    $('#continue').click(function(){
        $(this).hide();
        $('#texto p').html('')
        $('.opinar').show();
        continuar()

    })

    atualizarContador = function(){
        $('.validas').html(validas)
        $('.total').html(totalAtual)
    }

    validar = function(resposta){
        if(total == totalAtual){
            finalizar()
        }
        else{
            $('.opinar').hide()
            $('#continue').show()
        }
        $('#texto p').html(questionAtual.fields.texto)
        atualizarContador();
    }

    continuar = function(){
        $('.opinar').show()
        $('#texto p').html('')
        $('#continue').hide()
        atual++;
        question();
    }

    question = function(){     
        questionAtual = questions[atual];
        if(typeof questionAtual == 'undefined'){
            finalizar()
            return false
        }
        $('.all').attr('style','background:url("/media/'+questionAtual.fields.imagem+'") no-repeat center')
        $('.all').addClass('alpha')
        $('#outro').html(questionAtual.fields.outro)
    };

    finalizar = function(){
        $('.opinar').hide()
        $('body').addClass('end')
        $('.all').removeAttr('style').removeClass('alpha')
    }

});