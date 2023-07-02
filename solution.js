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

// Ejercicio 2

function getBriefMessages(objectArray){
    if(objectArray.length === 0){
        return [];
    }

    const message = objectArray[0].message;
    let shortMessages = [];

    if (message.length < 60){
        shortMessages.push(message);
    }

    const nextMessage = objectArray.slice(1);
    
    return shortMessages.concat(getBriefMessages(nextMessage));
}