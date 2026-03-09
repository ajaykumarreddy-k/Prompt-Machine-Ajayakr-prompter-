jsx
import { useState } from 'react';
import { Dialog, Transition } from '@headlessui/react';

const Modals = () => {
  const [createTaskOpen, setCreateTaskOpen] = useState(false);

  return (
    <div>
      {/* Trigger the modal */}
      <button
        onClick={() => setCreateTaskOpen(true)}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Open Create Task Modal
      </button>

      {/* Create Task Modal Component */}
      <CreateTaskModal isOpen={createTaskOpen} onClose={() => setCreateTaskOpen(false)} />
    </div>
  );
};

export default Modals;
