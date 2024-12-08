describe("Any", () => {
  it("should support in typescript", () => {
    const person: any = {
      id: 1,
      name: "Ahmad Dani",
      age: 18,
    };

    person.age = 16;
    person.addres = "Indonesia";
    console.info(person);
  });
});
