describe("Function", () => {
  it("should support in typescript", () => {
    function sayHello(name: string): string {
      return `Hello ${name}`;
    }

    expect(sayHello("Dani")).toBe("Hello Dani");

    function printHello(name: string): void {
      console.info(`Hello ${name}`);
    }

    printHello("Danii");
  });

  it("should support default value", () => {
    function sayHello(name: string = "Guest"): string {
      return `Hello ${name}`;
    }

    expect(sayHello("Dani")).toBe("Hello Dani");
    expect(sayHello()).toBe("Hello Guest");
  });

  it("should support rest parameter", () => {
    function sum(...values: number[]): number {
      let total = 0;
      for (const value of values) {
        total += value;
      }

      return total;
    }

    expect(sum(1, 2, 3, 4, 5)).toBe(15);
  });

  it("should support optional parameter", () => {
    function sayHello(firsname: string, lastname?: string): string {
      if (lastname) {
        return `Hello ${firsname} ${lastname}`;
      } else {
        return `Hello ${firsname}`;
      }
    }

    expect(sayHello("Ahmad")).toBe("Hello Ahmad");
    expect(sayHello("Ahmad", "Dani")).toBe("Hello Ahmad Dani");
  });

  it("should support function overloading", () => {
    function callMe(value: string): string;
    function callMe(value: number): number;
    function callMe(value: any) {
      if (typeof value === "string") {
        return value.toUpperCase();
      } else if (typeof value === "number") {
        return value * 10;
      }
    }

    expect(callMe("Hello")).toBe("HELLO");
    expect(callMe(10)).toBe(100);
  });

  it("should function as parameter", () => {
    function sayHello(name: string, filter: (name: string) => string): string {
      return `Hello ${filter(name)}`;
    }

    function toUpper(name: string): string {
      return name.toUpperCase();
    }

    expect(sayHello("Dani", toUpper)).toBe("Hello DANI");
    expect(
      sayHello("Dani", function (name: string): string {
        return name.toUpperCase();
      })
    ).toBe("Hello DANI");
    expect(sayHello("Dani", (name: string): string => name.toUpperCase())).toBe(
      "Hello DANI"
    );
  });
});
