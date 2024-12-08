import { configureStore, createAction, createReducer } from "@reduxjs/toolkit";

const addToCart = createAction("ADD_TO_CART");

// reducer
const initialState = {
  cart: [],
};

const cartReducer = createReducer([], (builder) => {
  builder.addCase(addToCart, (state, action) => {
    state.push(action.payload);
  });
});

const login = createAction("CREATE_SESSION");

const loginReducer = createReducer({ status: false }, (builder) => {
  builder.addCase(login, (state, action) => {
    state.status = true;
  });
});

// store
const store = configureStore({
  reducer: {
    cart: cartReducer,
    login: loginReducer,
  },
});
console.info("oncreate store: ", store.getState());

// dispatch
store.subscribe(() => {
  console.info("STORE CHANGE: ", store.getState());
});

store.dispatch(addToCart({ id: 1, qty: 3 }));
store.dispatch(addToCart({ id: 2, qty: 3 }));
store.dispatch(login());
