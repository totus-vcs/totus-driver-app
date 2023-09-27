import Atropos from 'atropos/react';


export default function () {

    return (
        <section className="py-4 mb-3">
            <div className="container pt-lg-3">



                {/* Intoducing the future of logistics */}

                <div className="row flex-lg-nowrap">
                    <div className="col-lg-6 col-xl-5 text-center text-lg-start pt-0 mt-xl-4">
                        <h1 className="display-4 pt-5 pb-2 pb-lg-3 mt-sm-2 mt-lg-5">
                            Introducing the future of logistics.
                        </h1>

                        <p className="fs-lg mb-4 mb-lg-5">
                        In the booming e-commerce landscape, where truck transport is pivotal in Australia, logistics faces heighter demands than ever before.
                        </p>
                        <h6 className="fs-lg mb-4 mb-lg-5">
                        TOTUS is an ingenious add-on for existing trucks, featuring remote acceleration and steering, 360 degree vision, and safety enhancements.

                        </h6>
                        <p className="fs-lg mb-4 mb-lg-5">
                        A retrofit solution, empowering logistics with reliability and drivers with an exceptional remote driving journey.
                        </p> 
                        
{/*                         
                        <p className="fs-lg mb-4 mb-lg-5">
                            With the e-commerce industry significantly expanding, and the huge reliance on trucks for transport of 
                            goods in Australia, the logistics company is under more pressure than ever before. 
                            The COVID-19 pandemic has put even more strain on the industry - now there are less truck drivers, and more truck drivers
                            wanting to spend time at home with their family. 
                        </p>
                        <h6 className="fs-lg mb-4 mb-lg-5">
                            The TOTUS project aims to fix this - by enabling the remote operation of
                            trucks, vehicles and industrial systems.
                        </h6>
                        <p className="fs-lg mb-4 mb-lg-5">
                            We are developing an innovative solution, an easy to install mechanism on exsiting trucks
                            with remote control acceleration and steering, as well as a range of sensors and safety features, to give
                            the logistics industry a reliable solution, and give drivers an optimal experience in remote control driving.
                        </p> */}

                        <a
                            href="https://anu365-my.sharepoint.com/:f:/r/personal/u6986400_anu_edu_au/Documents/ENGN4300-TOTUS%20(2023)?csf=1&web=1&e=vrCmNb"
                            className="btn btn-primary btn-lg"
                        >
                            View Repository &nbsp;
                            <i className="bx bx-cloud"></i>
                        </a>


                    </div>

                    <div className="col-lg-8 col-xl-8 text-center text-lg-start pt-3 mt-xl-4">

                        <Atropos className="atropos-banner" highlight={false} shadow={false} onEnter={() => console.log('enter')}>
                            <img className="atropos-banner-spacer" src="assets/img/landing_blank_canvas.png" alt="" />
                            <img data-atropos-offset="-3.5" src="assets/img/map_rotated.png" alt="" />
                            <img data-atropos-offset="3" src="assets/img/truck_vector_big_background.png" alt="" stretchX="50" />
                        </Atropos>
                    </div>


                </div>



            </div>



        </section>
    )
}