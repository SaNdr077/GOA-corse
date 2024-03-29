// 1) მოხმარებელი შემოიტანს რიცხვს, თუ ის იქნება უარყოფითი
//  რიცხვი უნდა დაგვიბრუნოს უარყოფითი რიცხვი, თუ ის იქნება
//   დადებითი რიცხვი დაგვიბრუნოს უარყოფითი რიცხვი, ყველა 
//   შემთხვევაში გვიბრუნებს უარყოფით რიცხვს გარდა ნულისა

let userNamber = prompt("enter numbr: ")
if (userNamber < 0){
    console.log(userNamber)
}else if (userNamber > 0){
    console.log(userNamber * -1)
}else{
    console.log("zero")
}
