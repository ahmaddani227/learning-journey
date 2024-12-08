import { Category, Product } from "../src/type-alias";

describe("Type Alias", () => {
  it("should support in typescript", () => {
    const category: Category = {
      id: 1,
      name: "Handphone",
    };

    const product: Product = {
      id: "1",
      name: "Xiaomi Redmi",
      price: 2500000,
      category: category,
    };

    console.info(category);
    console.info(product);
  });
});
