
function jscalc(e, baseprice) {
    this.targetElement = e
    this.pricelist = []
    for (var i = 0; i < baseprice.length; i++) {
        pricelist[i] = [
            {
                concept: 'Base',
                amount: baseprice[i],
                type: '$'
            }
        ]
    }

    this.updateListDisplay = function () {
        function createEvent(n) {
            return function(event) {
                createOverlay(n)
            }
        }
        e.empty()

        var subtotal = 0
        for (var i = 0; i < this.pricelist.length; i++) {
            var daysubtotal = 0
            for (var j = 0; j < this.pricelist[i].length; j++) {
                var data = this.pricelist[i][j]
                if (data.type == '$') {
                    daysubtotal = daysubtotal + data.amount
                }
                else if (data.type == '%') {
                    daysubtotal = daysubtotal * (1 + data.amount / 100)
                }
            }
            subtotal = subtotal + daysubtotal

            $('<tr>').click(
                createEvent(i)
            ).appendTo(
                this.targetElement
            ).append(
                $('<td>').text('Día ' + (i + 1))
            ).append(
                $('<td>').text('$' + daysubtotal)
            )
        }
        $('<tr>').appendTo(
            this.targetElement
        ).append(
            $('<td>').text('Subtotal')
        ).append(
            $('<td>').text('$' + subtotal)
        )
    }

    this.updateListDetail = function (e, day) {
        e.empty()
        for (var i = 0; i < pricelist[day].length; i++) {
            var data = pricelist[day][i]
            var newcontent = (data.type == '$') ? ('$' + data.amount) : (data.amount + '%')

            $('<tr>').appendTo(
                e
            ).append(
                $('<td>').text(data.concept)
            ).append(
                $('<td>').text(newcontent)
            )
        }

        var typebtn = $('<button>').text(
            '$'
        ).click(
            function(event) {
                $(this).text(
                    ($(this).text() == '$') ? '%' : '$'
                )
            }
        )
        var concepttextbox = $('<input>').attr(
            {'type': 'text', 'placeholder': 'Concepto'}
        )
        var valuetextbox = $('<input>').attr(
            {'type': 'text', 'placeholder': 'Valor'}
        ).keypress(
            function(ev) {
                return /[0-9\-,\b]/.test(String.fromCharCode(ev.which))
            }
        )
        var addbtn = $('<button>').text(
            'Agregar'
        ).click(
            function() {
                var x = parseFloat(valuetextbox.val())
                if (x && concepttextbox.val() != '') {
                    pricelist[day].push(
                        {
                            concept: concepttextbox.val(),
                            amount: x,
                            type: typebtn.text()
                        }
                    )
                    updateListDetail(e, day)
                    updateListDisplay(targetElement)
                }
            }
        )

        $('<tr>').appendTo(e).append(
            $('<td>').append(concepttextbox).append(typebtn).append(valuetextbox)
        ).append(
            $('<td>').append(addbtn)
        )
    }

    this.createOverlay = function(day) {
        var subtable = $('<table>').css(
            {
                "background-color": "rgba(255,255,255, 1.0)",
                "margin": "100 auto 0 auto"
            }
        )

        this.updateListDetail(subtable, day)

        $('<div>').click(
            function(event) {
                if (this == event.target) {
                    $(this).remove()
                }
            }
        ).appendTo(
            $('body')
        ).css(
            {
                "position": "absolute",
                "left": "0",
                "top": "0",
                "width": "100%",
                "height": "100%",
                "background-color": "rgba(0, 0, 0, 0.8)"
            }
        ).append(
            subtable
        )
    }

    updateListDisplay()
}

