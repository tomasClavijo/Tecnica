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

// Ejercicio 3

function fillSummaries(objectArray){
    let result = [];

    function processObject(i){
        if (i === objectArray.length){
            return;
        }

        let message = objectArray[i].message;
        let messageLength = message.length;
        let newObject = null;

        if (messageLength < 60){
            newObject = {
                message: message,
                id : objectArray[i].id,
                trimmed: message
            };
        } else {
            let trimmed = message.slice(0, 60);
            newObject = {
                message: message,
                id: objectArray[i].id,
                trimmed: trimmed
            };
        }

        result.push(newObject);
        processObject(i + 1);
    }

    processObject(0);
    return result;
}

// Ejercicio 4

function addSummaries(stringArray){
    let result = [];

    function processString(i){
        if (i === stringArray.length){
            return;
        }

        let text = stringArray[i];
        let textLength = text.length;
        let newObject = null;

        if(textLength < 60){
            newObject = {
                message: text,
                trimmed: text
            };
        } else {
            let trimmed = text.slice(0, 60);
            newObject = {
                message: text,
                trimmed: trimmed
            };
        }

        result.push(newObject);
        processString(i + 1);
    }

    processString(0);
    return result;
}