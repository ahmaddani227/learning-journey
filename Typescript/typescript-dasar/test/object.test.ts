describe("Object", () => {
  it("should support in typescript", () => {
    const person: { id: string | number; name: string; hobbies?: string[] } = {
      id: 1,
      name: "Ahmad Dani",
    };

    console.info(person);

    person.id = "1";
    person.name = "Dani";

    console.info(person);
  });
});
