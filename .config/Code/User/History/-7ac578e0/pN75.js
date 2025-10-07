import express from "express";
import dotenv from "dotenv";
import connection from "./config/db";

const app = express();

dotenv.config({
    path: "./.env"
});

connection();