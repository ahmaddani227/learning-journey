const express = require("express");
const expressLayouts = require("express-ejs-layouts");
const {
  loadContact,
  findContact,
  addContact,
  cekDuplikat,
  deleteContact,
  updateContacts,
} = require("./utils/contacts");
const { body, validationResult, check } = require("express-validator");
const session = require("express-session");
const cookieParser = require("cookie-parser");
const flash = require("connect-flash");
const app = express();
const port = 3000;

// EJS
app.set("view engine", "ejs");
app.use(expressLayouts); // Third-party middleware
app.use(express.static("public")); // Build in Middleware
app.use(express.urlencoded({ extended: true }));

// konfigurasi flash
app.use(cookieParser("secret"));
app.use(
  session({
    cookie: { maxAge: 6000 },
    secret: "secret",
    resave: true,
    saveUninitialized: true,
  })
);
app.use(flash());

app.get("/", (req, res) => {
  res.render("index", {
    layout: "layouts/main-layout",
    title: "Halaman Home",
  });
});

app.get("/about", (req, res) => {
  res.render("about", {
    layout: "layouts/main-layout",
    title: "Halaman About",
  });
});

app.get("/contact", (req, res) => {
  const contacts = loadContact();
  res.render("contact", {
    layout: "layouts/main-layout",
    title: "Halaman Contact",
    contacts,
    msg: req.flash("msg"),
  });
});

app.get("/contact/add", (req, res) => {
  res.render("add-contact", {
    layout: "layouts/main-layout",
    title: "Form Tambah Data Contact",
  });
});

app.post(
  "/contact",
  [
    body("nama").custom((value) => {
      const duplikat = cekDuplikat(value);
      if (duplikat) {
        throw new Error("Nama contact sudah terdaftar");
      }

      return true;
    }),
    check("email", "Email tidak valid").isEmail(),
    check("noHp", "No Hp tidak valid").isMobilePhone("id-ID"),
  ],
  (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      // return res.status(400).json({ errors: errors.array() });
      res.render("add-contact", {
        title: "Form Tambah Data Contact",
        layout: "layouts/main-layout",
        errors: errors.array(),
      });
    } else {
      addContact(req.body);
      // kirimkan flash message
      req.flash("msg", "Data contact berhasil ditambahkan");
      res.redirect("/contact");
    }
  }
);

app.get("/contact/delete/:nama", (req, res) => {
  const contact = findContact(req.params.nama);

  // jika contact tidak ada
  if (!contact) {
    res.status(404);
    res.send("<h1>404</h1>");
  } else {
    deleteContact(req.params.nama);
    req.flash("msg", "Data contact berhasil dihapus");
    res.redirect("/contact");
  }
});

// form edit contact
app.get("/contact/edit/:nama", (req, res) => {
  const contact = findContact(req.params.nama);

  res.render("edit-contact", {
    layout: "layouts/main-layout",
    title: "Form Edit Data Contact",
    contact,
  });
});

app.post(
  "/contact/update",
  [
    body("nama").custom((value, { req }) => {
      const duplikat = cekDuplikat(value);
      if (value != req.body.oldNama && duplikat) {
        throw new Error("Nama contact sudah terdaftar");
      }

      return true;
    }),
    check("email", "Email tidak valid").isEmail(),
    check("noHp", "No Hp tidak valid").isMobilePhone("id-ID"),
  ],
  (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      res.render("edit-contact", {
        title: "Form Edit Data Contact",
        layout: "layouts/main-layout",
        errors: errors.array(),
        contact: req.body,
      });
    } else {
      updateContacts(req.body);
      req.flash("msg", "Data contact berhasil diubah");
      res.redirect("/contact");
    }
  }
);

app.get("/contact/:nama", (req, res) => {
  const contact = findContact(req.params.nama);
  res.render("detail", {
    layout: "layouts/main-layout",
    title: "Detail Contact",
    contact,
  });
});

app.use("/", (req, res) => {
  res.status(404);
  res.send("<h1>404</h1>");
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
