import { Customer, CustomerType } from "../src/enum";

describe("Enum", () => {
  it("should support in typescript", () => {
    const customer: Customer = {
      id: 1,
      name: "Ahmad Dani",
      type: CustomerType.GOLD,
    };

    console.info(customer);
  });
});
