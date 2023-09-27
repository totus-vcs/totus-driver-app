import TickListNew from "../../components/TickListNew";
import TickListNormal from "../../components/TickListNormal";
import CrossList from "../../components/CrossList";

export default function () {

    return (
        <section class="container py-5 my-md-2 my-lg-4 my-xl-5">
            <h2 class="h1 text-center pb-3 pb-md-4">Audit Tracking</h2>
            <div class="price-switch-wrapper mb-n2">
                <div class="table-responsive-xxl pt-md-3">
                    <div class="row flex-nowrap pb-4">

                        {/* Audit 1 */}
                        <div class="col">
                            <div class="card h-100 border-0 shadow-sm p-xxl-3">
                                <div class="card-body">
                                    <div class="d-flex align-items-center pb-2 pb-md-3 mb-4">
                                        <div class="ps-4">
                                            <h3 class="fs-lg fw-normal text-light opacity-70 mb-2"> March 2023 </h3>
                                            <h4 class="h3 text-light lh-1 mb-0">
                                                <span data-monthly-price>Audit 1</span>
                                                <span class="fs-sm fw-normal opacity-70"></span>
                                            </h4>
                                        </div>
                                    </div>
                                    <ul class="list-unstyled fs-sm pb-md-3 mb-3">
                                        <TickListNew item="Concept of Operations" />
                                        <CrossList item="Stakeholder Review" />
                                        <CrossList item="Scope Defined" />
                                        <CrossList item="Initial System Design" />
                                        <CrossList item="Hands-On Testing" />
                                        <CrossList item="Finalized System Design" />
                                        <CrossList item="Remotely Driving Car" />
                                    </ul>
                                </div>
                                <div class="card-footer border-0 pt-0 pb-4">
                                    <a
                                        href="https://anu365-my.sharepoint.com/:f:/g/personal/u6986400_anu_edu_au/EqbCu3xGd4VMrA4525YR_M4Bxb---VawQgqzuQNMeiWmMA?e=u6ijVN"
                                        class="btn btn-outline-primary w-100 mb-2">
                                        View Submission
                                    </a>
                                    <a
                                        href="https://anu365-my.sharepoint.com/:f:/g/personal/u6986400_anu_edu_au/EpY_72pmd-pKpDYttYUEoY0Bfq7MM_daENLZOo73FPbvEw?e=wXgaiH"
                                        class="btn btn-outline-primary w-100">
                                        View Feedback Review
                                    </a>
                                </div>
                            </div>
                        </div>

                        {/* Audit 2 */}
                        <div class="col">
                            <div class="card h-100 border-0 shadow-sm p-xxl-3">
                                <div class="card-body">
                                    <div class="d-flex align-items-center pb-2 pb-md-3 mb-4">
                                        <div class="ps-4">
                                            <h3 class="fs-lg fw-normal text-light opacity-70 mb-2"> June 2023 </h3>
                                            <h4 class="h3 text-light lh-1 mb-0">
                                                <span data-monthly-price>Audit 2</span>
                                                <span class="fs-sm fw-normal opacity-70"></span>
                                            </h4>
                                        </div>
                                    </div>
                                    <ul class="list-unstyled fs-sm pb-md-3 mb-3">
                                        <TickListNormal item="Concept of Operations" />
                                        <TickListNew item="Stakeholder Review" />
                                        <TickListNew item="Scope Defined" />
                                        <TickListNew item="Initial System Design" />
                                        <CrossList item="Hands-On Testing" />
                                        <CrossList item="Finalized System Design" />
                                        <CrossList item="Remotely Driving Car" />
                                    </ul>
                                </div>
                                <div class="card-footer border-0 pt-0 pb-4">
                                    <a
                                        href="https://anu365-my.sharepoint.com/:f:/g/personal/u6986400_anu_edu_au/EtU7WtjVRihEpo2c-rSuarABfsS4hVUROmKjQ_jyLZHn7Q?e=frAhF1"
                                        class="btn btn-outline-primary w-100 mb-2">
                                        View Design and Testing Folder
                                    </a>
                                    <a
                                        href="https://anu365-my.sharepoint.com/:f:/g/personal/u6986400_anu_edu_au/ErSDq3GNZQVLve-D1TvyuXEBm5pMssZLkPtW6zyvcAEFZg?e=ook5Hc"
                                        class="btn btn-outline-primary w-100 mb-2">
                                        View Research and Scoping Folder
                                    </a>
                                    <a
                                        href="https://anu365-my.sharepoint.com/:f:/g/personal/u6986400_anu_edu_au/Espp_gUWN3RMqpHnGrELzWkBHcB6P6gQgwF9bya0adt21A?e=hUdULP"
                                        class="btn btn-outline-primary w-100 mb-2">
                                        View Stakeholder Interviews
                                    </a>
                                </div>

                            </div>
                        </div>

                        {/* Audit 3 */}
                        <div class="col">
                            <div class="card h-100 border-0 bg-primary shadow-primary shadow-dark-mode-none p-xxl-3"                            >
                                <div class="card-body">
                                    <div class="d-flex align-items-center pb-2 pb-md-3 mb-4">
                                        <div class="ps-4">
                                            <h3 class="fs-lg fw-normal text-light opacity-70 mb-2"> September 2023 </h3>
                                            <h4 class="h3 text-light lh-1 mb-0">
                                                <span data-monthly-price> Audit 3 </span>
                                                <span class="fs-sm fw-normal opacity-70"></span>
                                            </h4>
                                        </div>
                                    </div>
                                    <ul class="list-unstyled fs-sm pb-md-3 mb-3">
                                        <TickListNormal item="Concept of Operations" />
                                        <TickListNormal item="Stakeholder Review" />
                                        <TickListNormal item="Scope Defined" />
                                        <TickListNormal item="Initial System Design" />
                                        <TickListNew item="Hands-On Testing" />
                                        <TickListNew item="Finalized System Design" />
                                        <CrossList item="Remotely Driving Car" />
                                    </ul>
                                </div>
                                <div class="card-footer border-0 pt-0 pb-4">
                                    <a
                                        href="https://anu365-my.sharepoint.com/:f:/g/personal/u6986400_anu_edu_au/EtU7WtjVRihEpo2c-rSuarABfsS4hVUROmKjQ_jyLZHn7Q?e=frAhF1"
                                        class="btn btn-light w-100 mb-2">
                                        View Planning Document
                                    </a>
                                </div>
                            </div>
                        </div>

                        {/* Audit 4 */}
                        <div class="col">
                            <div class="card h-100 border-0 shadow-sm p-xxl-3">
                                <div class="card-body">
                                    <div class="d-flex align-items-center pb-2 pb-md-3 mb-4">
                                        <div class="ps-4">
                                            <h3 class="fs-lg fw-normal text-light opacity-70 mb-2"> November 2023 </h3>
                                            <h4 class="h3 text-light lh-1 mb-0">
                                                <span data-monthly-price> Audit 4 </span>
                                                <span class="fs-sm fw-normal opacity-70"></span>
                                            </h4>
                                        </div>
                                    </div>
                                    <ul class="list-unstyled fs-sm pb-md-3 mb-3">
                                        <TickListNormal item="Concept of Operations" />
                                        <TickListNormal item="Stakeholder Review" />
                                        <TickListNormal item="Scope Defined" />
                                        <TickListNormal item="Initial System Design" />
                                        <TickListNormal item="Hands-On Testing" />
                                        <TickListNormal item="Finalized System Design" />
                                        <TickListNew item="Remotely Driving Car" />
                                    </ul>
                                </div>
                                <div class="card-footer border-0 pt-0 pb-4">
                                    <a
                                        href="https://anu365-my.sharepoint.com/:f:/g/personal/u7335615_anu_edu_au/EiEW3y3iUIBOms0XvTfQ828BOxyPFaKzqHCu3t-V_aBoSg?e=SMeYaO"
                                        class="btn btn-outline-primary w-100">
                                        View Planning Document
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    )
}
