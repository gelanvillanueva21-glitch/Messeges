

import { useMutation } from "@tanstack/react-query";
import { Link } from "react-router-dom";
import React, { useState } from "react";
import type { RegisterPayload } from "../../types/Payload/User";
import { register } from "../../types/IndexApi";


export const SignupForm = (): React.ReactElement => {
    const [fullName, setFullName] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [showPassword, setShowPassword] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);


    const mutation = useMutation({
        mutationFn: (data: RegisterPayload) =>
            register(data)
    })

    function submitHandle() {

        if (fullName.length <= 8) {
            setErrorMessage("Name must at least 8 characters");
            return;
        }

        if (username.length <= 8) {
            setErrorMessage("Username must at least 8 characters");
            return;
        }

        if (password.length <= 8) {
            setErrorMessage("Password must at least 8 characters");
            return;
        }

        if (password !== confirmPassword) {
            setErrorMessage("Password and confirm password does not match.");
            return;
        }


    }

    return (
        <section className="min-h-screen flex items-center justify-center bg-slate-50 px-4 py-12 sm:px-6 lg:px-8">
            <form className="w-full max-w-md space-y-6 rounded-2xl bg-white p-8 shadow-xl border border-slate-100">
                <div className="text-center space-y-2">
                    <h1 className="text-3xl font-bold tracking-tight text-slate-900">
                        Sign Up.
                    </h1>
                    <p className="text-sm text-slate-500">
                        Create your account for Simple Messenger app.
                    </p>
                </div>

                <div className="space-y-4">
                    <label className="block text-sm font-medium text-slate-700 mb-1">
                        Full Name
                    </label>
                    <input 
                        type="text"
                        onChange={(e) => setFullName(e.target.value)}
                        className="w-full rounded-lg border border-slate-300 px-3.5 py-2.5 text-slate-900 placeholder-slate-400 focus:border-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-600/20 text-sm transition-all"
                        placeholder="Gelan Mar Villanueva"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-slate-700 mb-1">
                        Username
                    </label>
                    <input 
                        type="text" 
                        onChange={(e) => setUsername(e.target.value)}
                        className="w-full rounded-lg border border-slate-300 px-3.5 py-2.5 text-slate-900 placeholder-slate-400 focus:border-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-600/20 text-sm transition-all"
                        placeholder="JohnPork123"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-slate-700 mb-1">
                        Password
                    </label>
                    <input 
                        type={showPassword ? "text" : "password"}
                        onChange={(e) => setPassword(e.target.value)}
                        className="w-full rounded-lg border border-slate-300 px-3.5 py-2.5 text-slate-900 placeholder-slate-400 focus:border-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-600/20 text-sm transition-all"
                        placeholder="********"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-slate-700 mb-1">
                        Confirm Password
                    </label>
                    <input 
                        type={showPassword ? "text" : "password"}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        className="w-full rounded-lg border border-slate-300 px-3.5 py-2.5 text-slate-900 placeholder-slate-400 focus:border-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-600/20 text-sm transition-all"
                        placeholder="*******"
                    />
                </div>

                {errorMessage || mutation.error && (
                    <p>
                        {errorMessage? errorMessage : mutation.error.message}
                    </p>
                )}

                <div className="flex items-center gap-2 pt-1">
                    <input 
                        type="checkbox" 
                        onChange={(e) => setShowPassword(e.target.checked)}
                        id="show-password"
                        className="h-4 w-4 rounded border-slate-300 text-indigo-600 focus:ring-indigo-600/20 accent-indigo-600 cursor-pointer"

                    />
                    <label
                        htmlFor="show-password"
                        className="text-sm text-slate-600 cursor-pointer select-none">
                        {showPassword ? "Hide Password." : "Show Password"}
                    </label>
                </div>

                <button
                    type="submit"
                    onClick={submitHandle}
                    className="w-full rounded-lg bg-indigo-600 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 transition-colors"
                >

                </button>

                <div className="text-center pt-2 border-t border-slate-100">
                    <p className="text-sm text-slate-600">
                        Already have an account?{' '} 
                        <Link 
                        to={"/sign-in"} 
                        className="font-semibold text-indigo-600 hover:text-indigo-500 transition-colors"
                        >
                            Sign In.
                        </Link>
                    </p>
                </div>
            </form>
        </section>
    )
}

