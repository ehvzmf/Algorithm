/**
 * @param {number} days
 * @param {number[][]} meetings
 * @return {number}
 */
var countDays = function(days, meetings) {
    meetings.sort((s, e) => s[0] - e[0]); // sort by start day

    let busy = 0;
    let prevEnd = 0;

    for (let [start, end] of meetings) {
        if (start > prevEnd + 1) {
            busy += (start - prevEnd - 1);
        }
        prevEnd = Math.max(prevEnd, end);
    }

    let answer = days - (prevEnd - busy);
    return answer;
};