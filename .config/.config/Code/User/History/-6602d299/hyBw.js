import mongoose from "mongoose";
import dotenv from "dotenv";

dotenv.config({
    path: "./.env"
})

const connection = async () => {
    try{
        const conn = await mongoose.connect(process.env.MONGODB_URL);
        console.log("Mongodb connected");
        
    }
    catch(err){
        console.log(`Error ${err}`);
        process.exit(1)        
    }
};

export default connection;