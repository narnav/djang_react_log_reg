import React, { useEffect, useState } from "react";
import axios from "axios";
const Register = () => {
    const SERVER = "http://127.0.0.1:8000/";
    const [username, setuname] = useState("")
    const [password, setpassword] = useState("")
    const [email, setemail] = useState("a@a.com")
    const [msg, setmsg] = useState("")
    const reg = () => {
        axios.post(SERVER + "register", { username, password,email }).then((res) => setmsg(res.data));
    };
    return (
        <div>Register
            
            <h1 style={{ textAlign: "center" }}>
            {msg}</h1>
            <hr/>
            User name: <input onChange={(e) => setuname(e.target.value)} />
            Password: <input onChange={(e) => setpassword(e.target.value)} />
            email: <input onChange={(e) => setemail(e.target.value)} />
            <button onClick={() => reg()}>Register</button>
        </div>
    )
}

export default Register