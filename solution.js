// Ejercicio 1

function countWordLengths(wordArray){
    const hashWordLengths = {};

    function count(i){
        const word = wordArray[i];

        if(word){
            const kay = word.length;
            if(hashWordLengths[kay]){
                hashWordLengths[kay]++;
            } else{
                hashWordLengths[kay] = 1;
            }
        } else {
            return;
        }
        count(i+1);
    }

    count(0);
    return hashWordLengths;
}
