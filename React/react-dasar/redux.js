import { legacy_createStore } from "redux";

// reducer
const cartReducer = (state = { cart: [{ id: 1, qty: 2 }] }, action) => {
  switch (action.type) {
    case "ADD_TO_CART":
      return {
        ...state,
        cart: [...state.cart, action.payload],
      };
    default:
      return state;
  }
};

// store(untuk menyimpan store nya)
const store = legacy_createStore(cartReducer);
console.info("oncreate store: ", store.getState());

// subscribe(melihat perubahan yang ada di store)
store.subscribe(() => {
  console.info("STORE CHANGE: ", store.getState());
});

// dispatch
const action1 = { type: "ADD_TO_CART", payload: { id: 2, qty: 3 } };
store.dispatch(action1);
