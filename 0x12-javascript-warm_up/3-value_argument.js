#!/usr/bin/node

let count = 0;
for(let element in process.argv){
    count++;
}
if(count <= 2){
    console.log("No argument");
}
else{
    console.log(process.argv[2]);
}
