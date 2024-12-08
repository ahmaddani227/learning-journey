export enum CustomerType {
  // default nilai ketika dikonversi adalah number tapi bisa diubah
  REGULAR = "REGULAR",
  GOLD = "GOLD",
  PLATINUM = "PLATINUM",
}

export type Customer = {
  id: number;
  name: string;
  type: CustomerType;
};
