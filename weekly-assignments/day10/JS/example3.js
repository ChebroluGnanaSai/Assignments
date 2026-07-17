let marks = [85, 42, 76, 91, 38, 67, 55, 29, 80, 49];
let noof_pass = 0,noof_failed = 0,top_mark = marks[0],least_mark = marks[0],top_student = 1,
least_student = 1;
for (let i = 0; i < marks.length; i++) {
    if (marks[i] > 42) {
        noof_pass++;
    } else {
        noof_failed++;
    }
    if (marks[i] > top_mark) {
        top_mark = marks[i];
        top_student = i + 1;
    }
    if (marks[i] < least_mark) {
        least_mark = marks[i];
        least_student = i + 1;
    }
}
console.log("Least Mark:", least_mark);
console.log("Least Mark Student:", least_student);
console.log("Total Passed:", noof_pass);
console.log("Total Failed:", noof_failed);
for(let i=0;i<marks.length;i++){
    console.log("Student ",i+1,":",marks[i]);
}
console.log("Class Top is Student:", top_student);
console.log("Top Mark:", top_mark);
