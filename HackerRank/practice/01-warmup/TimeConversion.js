process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function timeConversion(s) {
    let res = '';

    let splitted = s.split(':', 3);
    let isAM = s.includes('AM') ? true : false;
    if (splitted[0] === '12') {
        if (isAM ) {
            splitted[0] = '00';
        }
    } else {
        if (!isAM) {
            splitted[0] = (parseInt(splitted[0]) + 12).toString();
        }
    }
    res = splitted[0] + ':' + splitted[1] + ':' + splitted[2];
    res = res.slice(0,8);
    return res;
}

function main() {
    var s = readLine();
    var result = timeConversion(s);
    process.stdout.write("" + result + "\n");

}
