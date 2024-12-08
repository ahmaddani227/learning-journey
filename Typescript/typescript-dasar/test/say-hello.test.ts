import { sayHello } from "../src/say-hello";

describe("sayHello", function () {
  it("should return hello dani", function () {
    expect(sayHello("dani")).toBe("Hello dani");
  });
});
