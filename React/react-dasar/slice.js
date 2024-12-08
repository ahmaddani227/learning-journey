import { configureStore, createSlice } from "@reduxjs/toolkit";

const cartSlice = createSlice({
  name: "cart",
  initialState: [],
  reducers: {
    addToCart(state, action) {
      state.push(action.payload);
    },
  },
});

// store
const store = configureStore({
  reducer: {
    cart: cartSlice.reducer,
  },
});

console.info("oncreate store: ", store.getState());

store.subscribe(() => {
  console.info("STORE CHANGE: ", store.getState());
});

store.dispatch(cartSlice.actions.addToCart({ id: 1, qty: 10 }));
