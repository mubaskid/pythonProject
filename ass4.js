function CapitalizeWord(words) {
    words = words.split(' ');

    for (let i = 0; i < words.length; i++) {

        words[i] = words[i][0].toUpperCase() + words[i].substr(1);

    }else
    return words.join(" ");
}

console.log(CapitalizeWord("hello world i am here"));