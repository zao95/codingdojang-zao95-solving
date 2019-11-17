class PersonClass {
    // PersonType 생성자와 동일합니다.
    constructor(name) {
        this.name = name;
    }
    // PersonType.prototype.sayName과 동일합니다.
    sayName() {
        console.log(this.name);
    }
}
let person = new PersonClass("Nicholas");
person.sayName();   // outputs "Nicholas"
console.log(person instanceof PersonClass);     // true
console.log(person instanceof Object);          // true
console.log(typeof PersonClass);                    // "function"
console.log(typeof PersonClass.prototype.sayName);  // "function"