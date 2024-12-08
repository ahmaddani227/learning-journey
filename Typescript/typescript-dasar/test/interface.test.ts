import { Employee, Manager } from "../src/embloyee";
import { Seller } from "../src/seller";

describe("Interface", () => {
  it("should support in typescript", () => {
    const seller: Seller = {
      id: 1,
      name: "Toko ABC",
      nib: "34567",
      npwp: "12345",
    };

    seller.name = "Toko A";

    console.info(seller);
  });

  it("should support functioon interface", () => {
    interface AddFunction {
      (value1: number, value2: number): number;
    }

    const add: AddFunction = (value1: number, value2: number): number => {
      return value1 + value2;
    };

    expect(add(1, 2)).toBe(3);
  });

  it("should support indexable interface", () => {
    interface StringArray {
      [index: number]: string;
    }

    const names: StringArray = ["upin", "ipin", "opet"];

    console.info(names[0]);
    console.info(names[1]);
    console.info(names[2]);
  });

  it("should support indexable interface for non number index", () => {
    interface StringDictonary {
      [key: string]: string;
    }

    const dictonary: StringDictonary = {
      name: "Ahmad Dani",
      addres: "Madura",
    };

    expect(dictonary["name"]).toBe("Ahmad Dani");
    expect(dictonary["addres"]).toBe("Madura");
  });

  it("should support extends interface", () => {
    const employee: Employee = {
      id: "1",
      name: "Ahmad Dani",
      division: "IT",
    };

    console.info(employee);

    const manager: Manager = {
      id: "2",
      name: "Dani",
      division: "IT",
      numberOfEmployees: 10,
    };
    console.info(manager);
  });

  it("should support function in interface", () => {
    const person: Person = {
      name: "Dani",
      sayHello: function (name: string): string {
        return `Hello ${name}, my name is ${this.name}`;
      },
    };

    console.info(person.sayHello("Upin"));
  });

  it("should support intersection types", () => {
    interface HasName {
      name: string;
    }

    interface HasId {
      id: string;
    }

    type Domain = HasName & HasId;

    const domain: Domain = {
      id: "1",
      name: "Dani",
    };

    console.info(domain);
    console.info(domain);
  });

  it("should support type assertions", () => {
    const person: any = {
      name: "Dani",
      age: 18,
    };

    const person2: Person = person as Person;
    // person2.sayHello("Upin"); //Error
    console.info(person2);
  });
});
