import TickListNew from "../../components/TickListNew";
import TickListNormal from "../../components/TickListNormal";
import CrossList from "../../components/CrossList";
import GreyBox from "../../components/GreyBox";
import OrangeBox from "../../components/OrangeBox";
import InvisiBox from "../../components/InvisiBox";

export default function () {

    return (
        <section class="container py-5 my-md-2 my-lg-4 my-xl-5">
            <h2 class="h1 text-center pb-3 pb-md-4">What's New in 2023?</h2>
            <div class="price-switch-wrapper mb-n2">
                <div class="table-responsive-xxl pt-md-3">

                    {/* HEADING ROW */}
                    <div class="row flex-nowrap pb-4">

                        <InvisiBox text="" />

                        <div class="col">
                            <div class="card h-100 border-0 shadow-sm p-xxl-3">
                                <div class="card-body">
                                    <div class="d-flex align-items-center pb-1 pb-md-3 mb-0">
                                        <div class="ps-4">
                                            <h3 class="fs-lg fw-normal text-light opacity-70 mb-2"> 2022 </h3>
                                            <h4 class="h3 text-light lh-1 mb-0">
                                                <span data-monthly-price>V1</span>
                                                <span class="fs-sm fw-normal opacity-70"></span>
                                            </h4>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="card h-100 border-0 bg-primary shadow-primary shadow-dark-mode-none p-xxl-3"                            >
                                <div class="card-body">
                                    <div class="d-flex align-items-center pb-2 pb-md-3 mb-0">
                                        <div class="ps-4">
                                            <h3 class="fs-lg fw-normal text-light opacity-70 mb-2"> 2023 </h3>
                                            <h4 class="h3 text-light lh-1 mb-0">
                                                <span data-monthly-price> V2 </span>
                                                <span class="fs-sm fw-normal opacity-70"></span>
                                            </h4>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="card h-100 border-0 shadow-sm p-xxl-3">
                                <div class="card-body">
                                    <div class="d-flex align-items-center pb-2 pb-md-3 mb-0">
                                        <div class="ps-4">
                                            <h3 class="fs-lg fw-normal text-light opacity-70 mb-2"> Future </h3>
                                            <h4 class="h3 text-light lh-1 mb-0">
                                                <span data-monthly-price>Final Product</span>
                                                <span class="fs-sm fw-normal opacity-70"></span>
                                            </h4>
                                        </div>
                                    </div>

                                </div>
                            </div>
                        </div>


                    </div>
                    {/* Final Output */}
                    <div class="row flex-nowrap pb-4">

                        <InvisiBox text="Main Project Output" />
                        <GreyBox items={<TickListNew item="Proof of Concept on Ford Focus" />} />
                        <OrangeBox items={<TickListNew item="Proof of Concept on Ford Focus" />} />
                        <GreyBox items={<TickListNew item="Finalized system retrofitted to trucks." />} />

                    </div>

                    {/* Mechanical System */}
                    <div class="row flex-nowrap pb-4">

                        <InvisiBox text="Mechanical System" />
                        <GreyBox items={<div>
                            <TickListNew item="Steering Control: Individual Component, broken after testing." />
                            <TickListNew item="Pedal Control: Individual Component, broken after testing." />
                            <CrossList item="Transmission and Reverse: Out of Scope." />
                        </div>} />
                        <OrangeBox items={<div>
                            <TickListNew item="Steering Control: Improving designs durability and functionality." />
                            <TickListNew item="Pedal Control: Improving designs durability and functionality." />
                            <CrossList item="Transmission and Reverse: Out of Scope." />
                        </div>} />
                        <GreyBox items={<div>
                            <TickListNew item="Steering Control" />
                            <TickListNew item="Pedal Control" />
                            <TickListNew item="Transmission and Reverse" />
                            <TickListNew item="All components retrofittable and removeable, still allows drivers to drive car while system is implemented." /> 
                        </div>} />

                    </div>

                    {/* Visual System */}
                    <div class="row flex-nowrap pb-4">

                        <InvisiBox text="Visual System" />
                        <GreyBox items={<div>
                            <TickListNew item="Singular camera, front view of car." />
                            <TickListNew item="Research into Lidar, Mapping, speedometer. " />
                            <CrossList item="Computer Vision: Out of Scope." />
                        </div>} />
                        <OrangeBox items={<div>
                            <TickListNew item="Multi camera, increased viewing range." />
                            <CrossList item="Additional Sensors: Out of Scope" />
                            <TickListNew item="Computer Vision Hazard Detection System - Stretch Goal" />
                        </div>} />
                        <GreyBox items={<div>
                            <TickListNew item="Full 360 degree viewing range. " />
                            <TickListNew item="Full research and application of additional sensors and mapping systems." />
                            <TickListNew item="Computer vision hazard system, with failsafe mechanisms in place. " />
                        </div>} />

                    </div>

                    {/* Software and Control */}
                    <div class="row flex-nowrap pb-4">

                        <InvisiBox text="Software and Control" />
                        <GreyBox items={<div>
                            <TickListNew item="Individual component control" />
                            <TickListNew item="4G remote connection" />
                            <CrossList item="Visual Interface: Out of Scope." />
                        </div>} />
                        <OrangeBox items={<div>
                            <TickListNew item="Simultaneous component control" />
                            <TickListNew item="5G Remote Connection" />
                            <TickListNew item="Visual Interface primarily for control during testing." />
                            <TickListNew item="Failsafe mechanisms for components within scope" />
                        </div>} />
                        <GreyBox items={<div>
                            <TickListNew item="Simultaneous component control" />
                            <TickListNew item="Ultra low latency connection, beyond current 4G and 5G technologies." />
                            <TickListNew item="Full user interface, user testing with truck drivers, logistics companies able to monitor and track driver behaviour. " />
                            <TickListNew item="Full safety analysis and failsafe mechanisms for entire system." />
                        </div>} />

                    </div>

                </div>
            </div>

        </section >

    )
}
