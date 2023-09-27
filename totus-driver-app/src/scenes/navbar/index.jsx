import { Link } from "react-router-dom";

const Navbar = () => {
    return (

        <section className="container py-1 my-md-3 my-lg-2">
            <nav className="navbar bg-body-tertiary ">

                {/* LOGO */}
                <div className="justify-content-start">
                    <a className="pt-3" href="/">
                        <img
                            src="assets/img/Totus_FRONT.png"
                            width="90"
                            alt="Totus Logo"
                        />
                        <img
                            src="assets/img/Totus_REAR.png"
                            width="200"
                            alt="Totus Text"
                        />
                    </a>
                </div>

                {/* {/* Right align buttons  */}
                <form className="justify-content-end">

                    <Link className="btn btn-sm btn-outline-primary me-2" type="button" onClick={TurnOn}>
                        Turn On System
                    </Link>

                    <Link className="btn btn-sm btn-outline-primary me-2" type="button" to="/media">
                        Media
                    </Link>
                    {/* 
                <Link className="btn btn-sm btn-outline-primary me-2" type="button" to="/contents">
                    Contents
                </Link> */}

                    <a className="btn btn-sm btn-outline-secondary" type="button" href="https://anu365-my.sharepoint.com/:f:/r/personal/u6986400_anu_edu_au/Documents/ENGN4300-TOTUS%20(2023)?csf=1&web=1&e=vrCmNb">
                        Repository
                    </a>

                </form>
            </nav>
        </section >
    )
}


export default Navbar;

async function TurnOn() {
    console.log('The link has been clicked.');

    // URL to which you want to send the POST request
    const url = 'http://10.0.0.202:5000/accellerator/turn_off';

    // Data to send in the request body (in JSON format)
    const data = {
        state: false, 
        speed: 30
    };

    // Options for the fetch request
    const options = {
        method: 'PUT',
        headers: { "Content-type": "application/json; charset=UTF-8" },
        body: JSON.stringify({ data }) // Convert the data to JSON string
    };

    const response = await fetch(url, options); 
    const response_data = await response.json(); 
    // Perform the POST request
    // await fetch(url, options)
    //     .then(response => {
    //         if (!response.ok) {
    //             throw new Error('Network response was not ok');
    //         }
    //         return response.json(); // Parse the JSON response
    //     })
    //     .then(responseData => {
    //         console.log('PUT request successful:', responseData);
    //     })
    //     .catch(error => {
    //         console.error('PUT request error:', error);
    //     });
}
