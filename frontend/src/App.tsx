

import React from 'react';
import { Routes, Route } from "react-router-dom";



export const App = ():React.ReactElement => {

    return (
        <main>
            <Routes>
            {/* PUBLic ROUTER FOR SIGN UP SIGN IN */}
                <Route/>
            {/* PRIVATE ROUTER ONLY THE PERSON SIGNIN */}
                <Route/>
            </Routes>
        </main>
    )
}

