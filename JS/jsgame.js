var grid = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    ]

var P1 = 'red'
var P2 = 'blue'

var turn = 'red'

function changeTurn() {
    if (turn == P1) {
        turn = P2
    } else {
        turn = P1
    }
}

function makeMove(button) {
    var positions = $(button).attr('pos').split(':')
    var list = positions[0]
    var index = grid[list].length

    var invalid = false
    while (grid[list][index] != 0) {
        index--
        if (index < 0) { invalid = true; break }
    }

    if (invalid) { alert('Movimento Inválido') } else {
    grid[list][index] = turn
    $('[pos="'+ list + ':' + index +'"]').css('background-color', turn)
    changeTurn()
    }
}



function makeGrid(grid) {
    for (var list = 0; list < grid.length; list++) {
        $('#board').append('<div class="grid_view" list="'+ list +'"></div>')
        for (var item = 0; item < grid[list].length; item++) {
            $('[list='+ list +']').append('<div class="item" pos="'+ list + ':' + item +'"></div>')
        }
    }
}

makeGrid(grid);

$('div[pos]').click(function () {
    makeMove($(this));
})