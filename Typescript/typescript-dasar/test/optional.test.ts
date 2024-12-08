describe("Optional Parameter", () => {
  it("should support in typescript", () => {
    function sayHello(name?: string | null) {
      if (name) {
        console.info(`Hello ${name}`);
      } else {
        console.info("Hello");
      }
    }

    sayHello("Ahmad Dani");
    const name: string | undefined = undefined;
    sayHello(name);
    sayHello(null);
  });
});
