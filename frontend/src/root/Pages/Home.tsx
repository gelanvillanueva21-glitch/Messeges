

import type React from "react";


export const Home = ():React.ReactElement => {


    return (
        <section>
            <div>
                {/* SO THIS IS THE SIDEBAR LIKE THE MESSENGER. */}

                <div>
                    {/* THIS DIV BOX IS FOR LOGO IMAGE AND NAME */}
                    <img 
                        src="" 
                        alt="" 
                    />
                    <h1>

                    </h1>
                </div>

                <div>
                    {/* 
                    THIS DIV HANDLE THE SEARCH BAR AND THE OUTPUT ASWELL WHEN CLICKED.  
                    IMPLEMENTING THE SEARCHED OUTPUT LATER ONWARDS.
                    */}
                    <img 
                        src="" 
                        alt="" 
                    />
                    <input 
                        type="text" 
                    />
                </div>

                <div>
                    {/* 
                    THIS DIV WILL HANDLE THE AVAILABLE USERS THAT YOU CAN CHAT.
                    IMPLEMENTING THE USERS LATER ONWARDS.
                    */}
                </div>
            </div>
            <div>
                {/* THIS IS THE CHAT WHERE YOULL SEE THERE CONVERSATION. */}

                <div>
                    {/* THIS DIV BOX WILL HANDLE THE NAME AND PROFILE DISPLAY AT THE TOP. */}
                    
                    <img 
                        src="" 
                        alt="" 
                    />
                    <h3>

                    </h3>
                </div>

                <div>
                    {/* THIS DIV BOX WILL HANDLE THE UL LIST OF THE CONVERSATION THEY HAD. */}
                    <ul>

                    </ul>
                </div>

                <div>
                    {/* THE INPUT BAR AT THE VERY BOTTOM */}

                    <img 
                        src="" 
                        alt="" 
                    />
                    <input 
                        type="text" 
                    />
                    <img 
                        src="" 
                        alt="" 
                    />
                </div>

            </div>
        </section>
    )
}

