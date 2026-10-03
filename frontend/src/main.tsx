

import { BrowserRouter } from "react-router-dom";
import ReactDom from "react-dom/client";
import { App } from "./App";
import { QueryClientProvider, QueryClient } from "@tanstack/react-query";


const queryClient = new QueryClient();


ReactDom.createRoot(document.getElementById("root")!).render(
    <QueryClientProvider client={queryClient}>
        <BrowserRouter>
            <App/>
        </BrowserRouter>
    </QueryClientProvider>
)


