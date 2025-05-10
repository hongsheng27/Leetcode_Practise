/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows > s.length || numRows === 1) return s;
    const arrays = Array.from({length: numRows}, ()=>'')
    let index = 0
    let direction = 1
     
    for(const elem of s){
        arrays[index]+=elem

        index += direction

        if( index === numRows - 1 || index === 0) {    
                direction = -direction 
        }
    }
    
    return arrays.join('')
};