describe("Union", () => {
  it("should support in typescript", () => {
    let sample: number | string | boolean = "Ahmad Dani";
    console.info(sample);

    sample = 100;
    console.info(sample);

    sample = true;
    console.info(sample);
  });

  it("should support typeof operator", () => {
    function process(value: number | string | boolean) {
      if (typeof value === "string") {
        return value.toUpperCase();
      } else if (typeof value === "number") {
        return (value += 2);
      } else {
        return !value;
      }
    }

    expect(process("dani")).toBe("DANI");
    expect(process(100)).toBe(102);
    expect(process(true)).toBe(false);
  });
});
