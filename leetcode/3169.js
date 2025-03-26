/**
 * @param {number} days
 * @param {number[][]} meetings
 * @return {number}
 */
var countDays = function(days, meetings) {
    meetings.sort((s, e) => s[0] - e[0]);

    for (let i=1; i<meetings.length; i++) {
        let [start, end] = meetings[i];
        let [prevStart, prevEnd] = meetings[i - 1];

        if (start <= prevEnd) {
            meetings[i][0] = prevStart;
            meetings[i][1] = Math.max(end, prevEnd);
        }

        if (prevStart !== meetings[i][0]) {
            days -= (prevEnd - prevStart + 1);
        }
    }
    answer = days - (meetings[meetings.length - 1][1] - meetings[meetings.length - 1][0] + 1);
    return answer
};