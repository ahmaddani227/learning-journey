describe("Array", () => {
  it("should same with javascript", () => {
    const names: string[] = ["upin", "ipin", "opet"];
    const values: number[] = [1, 2, 3];

    console.info(names);
    console.info(values);
  });

  it("should support readonly array", () => {
    const hobbies: ReadonlyArray<string> = ["Membaca", "Menulis"];
    console.info(hobbies);
    console.info(hobbies[0]);
    console.info(hobbies[1]);

    // hobbies[0] = "main game" //error
  });

  it("should support tuple", () => {
    const person: readonly [string, string, number] = ["Ahmad", "Dani", 18];

    console.info(person);
    console.info(person[0]);
    console.info(person[1]);
    console.info(person[2]);
  });
});
